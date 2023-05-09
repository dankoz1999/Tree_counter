from typing import List, Tuple


class Tree:
    def __init__(self, path: str) -> None:
        self.path = path

    def show_results(self) -> Tuple[str, str]:
        def read_file(path: str) -> List[List[int]]:
            lines = []
            with open(path) as f:
                lines = f.readlines()
            tree = []
            for line in lines:
                line = line.replace(" ", "")
                line = line.replace("\n", "")
                tmp = []
                for x in line:
                    tmp.append(int(x))
                tree.append(tmp)

            return tree

        def count_and_show_path(
            file: List[List[int]], possible_strings: List[str] = []
        ) -> str:
            def validate(
                possible_list: List[str], previous_list: List[int], results: List[int]
            ) -> List[str]:
                res: List[str] = []
                for i, pre in enumerate(previous_list):
                    word1 = str(pre) + possible_list[i]
                    word2 = str(pre) + possible_list[i + 1]
                    suma = 0
                    for letter in word1:
                        suma += int(letter)
                    if suma == results[i]:
                        res.append(word1)
                    else:
                        res.append(word2)

                return res

            t_file = file.copy()
            tmp_list = []
            if len(t_file) > 1:
                last_row = t_file[-1]
                pre_last = t_file[-2]
                for x in range(len(pre_last)):
                    tmp_list.append(
                        max(pre_last[x] + last_row[x], pre_last[x] + last_row[x + 1])
                    )
                    if len(possible_strings) < x + 1:
                        if pre_last[x] + last_row[x] > pre_last[x] + last_row[x + 1]:
                            possible_strings.append(str(pre_last[x]) + str(last_row[x]))
                        else:
                            possible_strings.append(
                                str(pre_last[x]) + str(last_row[x + 1])
                            )
                if len(possible_strings) > 0 and len(possible_strings) != len(file) - 1:
                    possible_strings = validate(possible_strings, pre_last, tmp_list)
                t_file[-2] = tmp_list
                t_file = t_file[:-1]
                if len(t_file) > 1:
                    return count_and_show_path(t_file, possible_strings)
                else:
                    return (t_file[0][0], possible_strings)
            return None

        file = read_file(self.path)
        res = count_and_show_path(file)
        return res


easy = Tree("2-easy.txt")
easy.show_results()
