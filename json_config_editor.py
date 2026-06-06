import json

FILE_NAME = "config.json"


def load_config():
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        return json.load(file)


def save_config(config):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(config, file, ensure_ascii=False, indent=2)


def show_config(config):
    print("当前配置：")
    for key, value in config.items():
        print(f"{key}: {value}")


def get_new_value(key):
    value = input("请输入新的值：").strip()
    if not value:
        print("新值不能为空")
        return None

    if key == "font_size":
        try:
            value = int(value)
        except ValueError:
            print("字体大小必须是数字")
            return None

        if not 8 <= value <= 32:
            print("字体大小必须在 8 到 32 之间")
            return None

    return value


def main():
    config = load_config()
    show_config(config)

    key = input("请输入要修改的设置：").strip()
    if key not in config:
        print("设置不存在")
        return

    value = get_new_value(key)
    if value is None:
        return

    config[key] = value
    save_config(config)
    print("保存成功")
    show_config(config)


if __name__ == "__main__":
    main()