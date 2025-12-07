from gdo.base.Exceptions import GDOError
from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_Object import GDT_Object
from gdo.core.GDT_User import GDT_User
from gdo.date.GDT_Created import GDT_Created


class GDO_LikeTable(GDO):

    def gdo_liked_table(self) -> GDO:
        raise GDOError('gdo_liked_table: Not implemented in '+self.fqcn())

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_Object('like_object').table(self.gdo_liked_table()).primary(),
            GDT_User('like_user').primary(),
            GDT_Created('like_created'),
        ]
