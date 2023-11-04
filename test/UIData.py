class UIData:
    def __init__(self, UI):

        self.ty_intellect = UI.ty_zhili
        self.in_intellect = UI.jt_zhili

        self.buff_amount = UI.buff_liang
        self.out_intellect = UI.zj_zhili
        self.out_lv = UI.zl_lv
        self.add = UI.add
        self.in_lv = UI.jt_lv
        self.ty_lv = UI.ty_lv
        self.ty3_lv = UI.ty3_lv
        self.halo_amount = UI.buff_gh
        self.pet_amount = UI.buff_cw
        self.jade_amount = UI.buff_bxy

        self.fixed_attack = UI.sg_guding
        self.fixed_intellect = UI.lz_guding

        self.percentage_attack = UI.sg_bfb
        self.percentage_intellect = UI.lz_bfb

        self.ty_fixed = UI.ty_lz
        self.ty_percentage = UI.ty_bfb

        self.out_medal = UI.zj_xz
        self.out_earp = UI.zj_eh
        self.out_passive = UI.zj_bd
        self.out_guild = UI.zj_gh
        self.nai_ba_guardian = UI.naiba_sh
        self.nai_ba_ssp = UI.naiba_ej

        self.cp_arms = UI.cp_arm
        #########################################

    def get_default_value(self):
        return {
            'ty_lv': 37,
            'ty_intellect': 0,
            'ty3_lv': 3,
            'buff_amount': 0,
            'out_intellect': 0,
            'out_lv': 1,
            'out_medal': 50,
            'out_earp': 175,
            'out_passive': 554,
            'out_guild': 80,
            'in_intellect': 0,
            'in_lv': 21,
            'halo_amount': 0,
            'pet_amount': 0,
            'jade_amount': 0,
            'fixed_attack': 0,
            'fixed_intellect': 0,
            'percentage_attack': [],
            'percentage_intellect': [],
            'ty_fixed': 0,
            'ty_percentage': [],
            'cp_arm': True,
            'nai_ba_guardian': 0,
            'nai_ba_ssp': 0,
        }

    def get_value(self, name):
        if name not in self.__dict__:
            raise print(f"{name} is not in UI")
        if name in ("percentage_attack", "percentage_intellect", "ty_percentage"):
            val = self.__dict__[name].text()
            return [float(i) for i in val.split(",")] if val else []
        elif name == "cp_arms":
            return self.__dict__[name].isChecked()
        else:
            return float(self.__dict__[name].text()) if self.__dict__[name].text() else 0

    def get_dict(self) -> dict:
        return {name: self.get_value(name) for name in self.__dict__}

    def __call__(self, name):
        return self.get_value(name)
