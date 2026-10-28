"""Run only from installed Blender: blender -b --python script -- --output /tmp/demo"""
import sys
from pathlib import Path

def main():
    try:import bpy
    except ImportError:raise SystemExit('Requires Blender Python (bpy).')
    args=sys.argv[sys.argv.index('--')+1:] if '--' in sys.argv else []
    out=Path(args[args.index('--output')+1]) if '--output' in args else Path('/tmp/disenador-clay-demo')
    out.parent.mkdir(parents=True,exist_ok=True)
    bpy.ops.object.select_all(action='SELECT');bpy.ops.object.delete(use_global=False)
    bpy.ops.mesh.primitive_uv_sphere_add(segments=48,ring_count=24,location=(0,0,1.2))
    obj=bpy.context.object;obj.name='Clay Monogram Base';obj.scale=(1,0.72,1);bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    bpy.ops.object.shade_smooth()
    mat=bpy.data.materials.new('Terracotta Clay');mat.diffuse_color=(0.9,0.34,0.22,1);mat.use_nodes=True
    bsdf=mat.node_tree.nodes.get('Principled BSDF');bsdf.inputs['Base Color'].default_value=(0.75,0.26,0.16,1);bsdf.inputs['Roughness'].default_value=0.83;obj.data.materials.append(mat)
    bpy.ops.mesh.primitive_cylinder_add(vertices=72,radius=1.25,depth=.18,location=(0,0,.13))
    base=bpy.context.object;base.name='Display Plinth';bpy.ops.object.shade_smooth()
    base_mat=bpy.data.materials.new('Plinth Chalk');base_mat.diffuse_color=(0.87,0.85,0.78,1);base.data.materials.append(base_mat)
    def track(o,point):o.rotation_euler=(point-o.location).to_track_quat('-Z','Y').to_euler()
    bpy.ops.object.camera_add(location=(3.9,-5.5,3.1));cam=bpy.context.object;track(cam,__import__('mathutils').Vector((0,0,1)));bpy.context.scene.camera=cam
    bpy.ops.object.light_add(type='AREA',location=(-3,-4,6));bpy.context.object.data.energy=780;bpy.context.object.data.shape='DISK';bpy.context.object.data.size=5
    sc=bpy.context.scene;sc.render.engine='CYCLES';sc.cycles.samples=48
    sc.render.resolution_x=1100;sc.render.resolution_y=1100;sc.render.resolution_percentage=100
    sc.render.image_settings.file_format='PNG';sc.render.film_transparent=True
    bpy.ops.wm.save_as_mainfile(filepath=str(out.with_suffix('.blend')))
    sc.render.filepath=str(out.with_suffix('.png'));bpy.ops.render.render(write_still=True)
    print(f'Saved {out.with_suffix(".blend")} and {out.with_suffix(".png")}')
if __name__=='__main__':main()
