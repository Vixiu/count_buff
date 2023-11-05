class UIData:
    def __init__(self):
        self.cp_arm = None
        self.fixed_attack = None
        self.jade_amount = None
        self.fixed_intellect = None
        self.percentage_attack = None
        self.percentage_intellect = None
        self.ty_fixed = None
        self.ty_percentage = None
        self.out_medal = None
        self.out_earp = None
        self.out_passive = None
        self.out_guild = None
        self.nai_ba_guardian = None
        self.nai_ba_ssp = None
        self.pet_amount = None
        self.halo_amount = None
        self.ty3_lv = None
        self.ty_lv = None
        self.in_lv = None
        self.add = None
        self.out_lv = None
        self.out_intellect = None
        self.buff_amount = None
        self.ty_intellect = None
        self.in_intellect = None

    def bind_input(self, UI):
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
        self.cp_arm = UI.cp_arm

    def get_value(self, name):
        if name not in self.__dict__:
            raise print(f"{name} is not in UI")

        if name in ("percentage_attack", "percentage_intellect", "ty_percentage"):
            val = self.__dict__[name].text()
            if val == '':
                val = self.__dict__[name].placeholderText()
            return [float(i) for i in val.split(",") if i] if val else []
        elif name in ("pet_amount", "halo_amount", "jade_amount"):
            val = self.__dict__[name].text()
            if val == '':
                val = self.__dict__[name].placeholderText()
            return float(val) if val else 0.0
        elif name == "cp_arm":
            return self.__dict__[name].isChecked()
        else:
            val = self.__dict__[name].text()
            if val == '':
                val = self.__dict__[name].placeholderText()
            return int(float(val)) if val else 0

    def get_values(self) -> dict:
        return {name: self.get_value(name) for name in self.__dict__}

    def set_value(self, name, value):
        try:
            if name not in self.__dict__:
                raise print(f"{name} is not in UI")
            if name in ("percentage_attack", "percentage_intellect", "ty_percentage"):
                self.__dict__[name].setText(",".join([str(i) for i in value]))
            elif name == "cp_arm":
                self.__dict__[name].setChecked(value)
            else:
                self.__dict__[name].setText(str(value))
        except Exception as e:
            print(e, name, value)

    def set_values(self, values: dict):
        for name, value in values.items():
            self.set_value(name, value)

    def set_placeholder_text(self, name, text):
        if name not in self.__dict__:
            raise print(f"{name} is not in UI")
        if name in ("percentage_attack", "percentage_intellect", "ty_percentage"):
            self.__dict__[name].setPlaceholderText(",".join([str(i) for i in text]))
            self.__dict__[name].setText('')
        elif name == "cp_arm":
            self.__dict__[name].setChecked(text)
        else:
            self.__dict__[name].setPlaceholderText(str(text))
            self.__dict__[name].setText('')

    def set_placeholder_texts(self, values: dict):
        for name, value in values.items():
            self.set_placeholder_text(name, value)

    def __call__(self, fn):
        def run_fn():
            return fn(self.get_values())

        return run_fn
