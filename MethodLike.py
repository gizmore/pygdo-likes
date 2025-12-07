from gdo.base.Exceptions import GDOException
from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.base.Method import Method
from gdo.core.GDT_Object import GDT_Object
from gdo.likes.GDO_LikeTable import GDO_LikeTable


class MethodLike(Method):

    def gdo_likes_table(self) -> GDO_LikeTable:
        raise GDOException("gdo_likes_table: Not implemented in "+self.fqcn())

    def gdo_liked_table(self) -> GDO:
        raise GDOException("gdo_liked_table: Not implemented in "+self.fqcn())

    def gdo_parameters(self) -> list[GDT]:
        return [
            GDT_Object('id').table(self.gdo_liked_table()).not_null(),
        ]

    def get_like_object(self) -> GDO:
        return self.param_value('id')

    def gdo_execute(self) -> GDT:
        object = self.get_like_object()
        self.gdo_likes_table().blank({
            'like_object': object.get_id(),
            'like_user': self._env_user.get_id(),
        }).soft_replace()
        return self.msg('msg_liked')
