import initial_function
import AutoCompleteModule


def main():
    print("Loading the files and preparing the system...")
    initial_function.read_from_zip()
    print("The system is ready. ")
    while True:
        text_to_search = input("Enter your text:\n").strip().lower()
        print(AutoCompleteModule.get_best_k_completions(text_to_search))
        another_text_to_search = input(text_to_search)
        while another_text_to_search != "#":
            text_to_search = (text_to_search + another_text_to_search).strip().lower()
            print(AutoCompleteModule.get_best_k_completions(text_to_search))
            another_text_to_search = input(text_to_search)


if __name__ == '__main__':
    main()
