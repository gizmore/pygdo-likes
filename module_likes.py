from gdo.base.GDO_Module import GDO_Module
from gdo.base.GDT import GDT
from gdo.core.GDT_UInt import GDT_UInt


class module_likes(GDO_Module):

    def gdo_module_config(self) -> list[GDT]:
        return [
        ]

    def gdo_user_config(self) -> list[GDT]:
        return [
            GDT_UInt('likes_given').initial('0'),
            GDT_UInt('likes_received').initial('0'),
        ]
