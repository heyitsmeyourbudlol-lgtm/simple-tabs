import bpy


_should_update_rename = True


def update_rename(self, context):
    global _should_update_rename
    if not _should_update_rename:
        return

    _should_update_rename = False
    if not self.rename:
        self.rename = self.name
    self.rename = self.rename.strip()
    _should_update_rename = True


class TabProps(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty(
        name='Original Name',
        description='The original name of this tab in the sidebar',
    )


    rename: bpy.props.StringProperty(
        name='Changed Name',
        description='The new name of this tab in the sidebar (clear to reset to default)',
        update=update_rename,
    )
