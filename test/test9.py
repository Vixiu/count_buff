def input_validation(fn):
    def validation(text: str):
        if ',' in text:
            try:
                return False, [eval(i) for i in text.split(',')]
            except:
                return False, "非法字符"
        else:
            try:
                ve = eval(text)
                if isinstance(ve, (int, float)):
                    return False, ve
                elif isinstance(ve, str) and (ve.startswith('+') or ve.startswith('-')):
                    return True, ve
                else:
                    return False, "非法字符"
            except:
                return False, "非法字符"

    def run_fn():
        global data_now

        def input_data(k: str):
            text = UI_DATA.get(k).text().replace(" ", "").replace("，", ',').replace("。", '.')
            if text != '':
                bl, ve = validation(text)
                if isinstance(ve, str):
                    exception.append((k, ve))
                elif bl and k not in ('percentage_intellect', 'percentage_attack', 'fixed_intellect', 'fixed_attack', 'jade_amount'):
                    data_now[k] = data_base[k] + ve
                else:
                    data_now[k] = ve

        for v in UI_DATA.values():
            v.setStyleSheet("")
        exception = []
        for keys in UI_DATA:
            input_data(keys)

        data_now['percentage_attack'] = [data_now['percentage_attack']] if not isinstance(data_now['percentage_attack'], list) else data_now['percentage_attack']
        data_now['percentage_intellect'] = [data_now['percentage_intellect']] if not isinstance(data_now['percentage_intellect'], list) else data_now['percentage_intellect']

        if not 0 < data_now['in_lv'] < 41:
            exception.append(('in_lv', '1~40'))
        if not 0 < data_now['out_lv'] < 41:
            exception.append(('out_lv', '1~40'))

        if exception:
            for key, tip in exception:
                UI_DATA[key].setText(tip)
                UI_DATA[key].setStyleSheet("font-size: 12px; background-color: #00aaff; border:0px; border-bottom: 3px solid red;")
        else:
            fn()

    return run_fn