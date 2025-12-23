def write_first_line_to_file(file_contents, output_filename):
    
    first_line = file_contents.split("\n")[0]
    with open(output_filename, "w") as f:
        f.write(first_line)


def read_even_numbered_lines(file_name):
 
    even_numbered_lines = list()
    with open(file_name) as f:
        lines = f.readlines()
  
        for index, line in enumerate(lines):
            if ((index + 1) % 2) == 0:
                even_numbered_lines.append(line)
    return even_numbered_lines


def read_file_in_reverse(file_name):
   
    with open(file_name) as f:
        lines = f.readlines()
        lines.reverse()
        print(lines)
        return lines


def main():
    # file_contents = read_file("sampletext.txt")
    # print(read_file_into_list("sampletext.txt"))
    # write_first_line_to_file(file_contents, "online.txt")
    print(read_even_numbered_lines("a.txt"))
    # print(read_file_in_reverse("sampletext.txt"))


if __name__ == "__main__":
    main()