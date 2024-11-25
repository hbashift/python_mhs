import argparse
from latex_generator_hbashift import generate_latex_table, generate_latex_image

def main(image_path, output_file):
    # Пример данных для таблицы
    data = [
        ["Name", "Age", "Country"],
        ["Alice", 30, "USA"],
        ["Bob", 25, "UK"],
        ["Charlie", 35, "Canada"]
    ]

    # Генерация LaTeX-кода для таблицы
    latex_code = generate_latex_table(data)

    # Генерация LaTeX-кода для изображения
    latex_image = generate_latex_image(image_path=image_path)

    # Запись кода в файл
    with open(output_file, "w") as f:
        f.write("\\documentclass{article}\n")
        f.write("\\usepackage[utf8]{inputenc}\n")
        f.write("\\usepackage{graphicx}\n")
        f.write("\\begin{document}\n")
        f.write(latex_code)
        f.write(latex_image)
        f.write("\n\\end{document}")

    print(f"LaTeX файл успешно сохранён в {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate LaTeX file with table and image.")
    parser.add_argument("image_path", help="Path to the image file to include in the LaTeX document.")
    parser.add_argument(
        "--output",
        default="example_table.tex",
        help="Path to save the generated LaTeX file (default: example_table.tex)."
    )
    args = parser.parse_args()

    main(image_path=args.image_path, output_file=args.output)
