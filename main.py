
PATH = "books/fr.txt"
def main():
    with open(PATH) as f:
        file_content = f.read()
        words = len(file_content.split())
        char_count = count_characters(file_content)
        char_list = [{"char": char, "num": count} for char, count in char_count.items()]
    
        # Sort the list of dictionaries by the "num" key in descending order
        char_list.sort(key=lambda x: x["num"], reverse=True)
        
        # Generate the report
        report = []
        report.append(f"--- Begin report of {PATH} ---")
        report.append("")
        
        for entry in char_list:
            report.append(f"The '{entry['char']}' character was found {entry['num']} times")
        
        report.append("--- End report ---")
        
        # Print the report
        for line in report:
            print(line)

def count_characters(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
    return char_count
main()