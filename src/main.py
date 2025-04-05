from jinja2 import Environment, FileSystemLoader
from translations.data import load_data
from pathlib import Path


languages = {"pt-br": "Português", "en": "English", "ja": "日本語"}
default_lang = "pt-br"

github_stats_custom_message = {
    "en": "My Github stats 👌",
    "pt-br": "Minhas estatísticas do Github 👌",
    "ja": "私のGithuの統計",
}

env = Environment(
    loader=FileSystemLoader("./templates/"), trim_blocks=True, lstrip_blocks=True
)


def main():
    print("Creating READMEs...")
    template = env.get_template("README.template.md")
    translations = load_data()

    # Delete READMEs in langs folder before creating them
    langs_folder = Path("../langs")
    for readme in langs_folder.glob("*"):
        readme.unlink()

    for lang in languages.keys():
        header_languages = {k: v for k, v in languages.items() if k != lang}

        output = template.render(
            tr=translations,
            lang=lang,
            default_lang=default_lang,
            header_langs=header_languages,
            custom_message=github_stats_custom_message[lang].replace(" ", "+"),
        )

        if lang == default_lang:
            output_path = Path("../README.md")
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(output)
        else:
            output_path = Path(f"../langs/README.{lang}.md")
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(output)
                
    print("READMEs created!")


if __name__ == "__main__":
    main()
