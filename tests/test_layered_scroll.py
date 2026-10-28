"""Smoke checks for V4 layered scrolling demo. Run: pytest -q tests/test_layered_scroll.py"""
from pathlib import Path
from shutil import which
import pytest
from playwright.sync_api import sync_playwright

FILE=Path(__file__).resolve().parents[1]/'examples'/'layered-scroll-v4.html'

@pytest.fixture(scope='module')
def browser():
    with sync_playwright() as p:
        b=p.chromium.launch(headless=True,executable_path=which('chromium') or None,args=['--no-sandbox'])
        yield b
        b.close()

@pytest.mark.parametrize('width,height', [(320,700),(375,812),(768,900),(1024,768),(1440,900)])
def test_chapters_mobile_and_desktop(browser,width,height):
    page=browser.new_page(viewport={'width':width,'height':height},device_scale_factor=1)
    errors=[]
    page.on('pageerror',lambda e:errors.append(str(e)))
    page.set_content(FILE.read_text(encoding='utf-8'),wait_until='load')
    assert page.title().startswith('DISEÑADOR V4')
    assert page.locator('.chapter').count()==3
    assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth + 1'), f'horizontal overflow at {width}'
    for id in ['materia','profundidad','ritmo']:
        page.locator(f'#{id}').scroll_into_view_if_needed()
        page.wait_for_timeout(80)
        assert page.locator(f'#{id} .stage').count()==1
        assert page.locator(f'#{id} .progress-line').get_attribute('style') is not None
    assert not errors,errors
    page.close()


def test_reduced_motion_and_keyboard(browser):
    page=browser.new_page(viewport={'width':375,'height':812},reduced_motion='reduce')
    page.set_content(FILE.read_text(encoding='utf-8'))
    assert page.locator('#materia .stage').evaluate("e => getComputedStyle(e).position") == 'relative'
    page.keyboard.press('Tab')
    assert page.evaluate('document.activeElement.classList.contains("skip")')
    page.locator('header a[href="#materia"]').click()
    assert page.evaluate('location.hash')=='#materia'
    assert page.locator('a[href="#profundidad"]').count() >= 1
    page.close()


def test_layer_progress_bidirectional(browser):
    page=browser.new_page(viewport={'width':1280,'height':800})
    page.set_content(FILE.read_text(encoding='utf-8'))
    section=page.locator('#materia')
    y=section.evaluate('e => e.offsetTop')
    distance=section.evaluate('e => e.offsetHeight - window.innerHeight')
    for fraction in [0.1,0.5,0.9,0.3]:
        page.evaluate('y => window.scrollTo({top:y,behavior:"instant"})',y+distance*fraction)
        page.wait_for_timeout(90)
        v=section.locator('.progress-line').evaluate('e => getComputedStyle(e).transform')
        assert v.startswith('matrix(')
        scale=float(v.split('(')[1].split(',')[0])
        assert abs(scale-fraction)<0.035,(scale,fraction)
    page.close()
