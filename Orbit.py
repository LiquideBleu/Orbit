##################################################################################################
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>
#
##################################################################################################

###                                                        ###
#                                                            #
# A simple Add-on to add Quick navigition option in 3D view. #
# Autor : Anthony Guiziou (LiquideBleu)                      #
#                                                            #
###                                                        ###


bl_info = {
    "name": "Orbit",
    "author": "Anthony Guiziou (liquideBleu)",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Sidebar > View > Orbit",
    "description": "A simple Add-on to add Quick navigation option in 3D view.",
    "warning": "",
    "wiki_url": "",
    "category": "User",
}

import bpy

# 3D view panel
class VIEW3D_PT_Orbit(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'View'
    bl_label = "Orbit"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        
        view = context.space_data
        
    # User preferences
        prefs  = context.preferences
        inputs = prefs.inputs
        
        row = layout.row()
        flow = layout.grid_flow()

    # Navigation
        flow.row().prop(inputs, "view_rotate_method", expand=True)
        flow.prop(inputs, "use_rotate_around_active")
        flow.prop(inputs, "use_mouse_depth_navigate")
        flow.prop(inputs, "use_zoom_to_mouse")
        flow.prop(inputs, "use_auto_perspective")


# registering and menu integration
def register():
    bpy.utils.register_class(VIEW3D_PT_Orbit)

# unregistering and removing menus
def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_Orbit)


if __name__ == "__main__":
    register()
