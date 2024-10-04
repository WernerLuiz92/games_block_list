import re

def process_subreddits(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Expressão regular para encontrar subreddits que começam com "r/"
    subreddits = re.findall(r'r/(\S+)', content)

    # Remover duplicatas e ordenar a lista
    unique_subreddits = sorted(set(subreddits))

    # Formatar a lista no estilo ||reddit.com/r/<subreddit>/*$all
    formatted_subreddits = [f"||reddit.com/r/{subreddit}/*$all" for subreddit in unique_subreddits]

    # Escrever a lista formatada no arquivo de saída
    with open(output_file, 'w', encoding='utf-8') as output:
        output.write('\n'.join(formatted_subreddits))

    print(f"Subreddits processados e salvos em {output_file}")

# Use os arquivos de entrada e saída desejados
input_file = 'subreddits.txt'  # Nome do arquivo de entrada com os subreddits
output_file = 'blocked_subreddits.txt'  # Nome do arquivo de saída

process_subreddits(input_file, output_file)
