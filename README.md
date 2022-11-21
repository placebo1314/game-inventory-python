# Game inventory

## Story

You just started working at a game development company named Eastwood Studios
and they decided to create a new text-based role-playing video game.
You are responsible for implementing the inventory system of the game, which stores,
shows, and manages goods the player acquires.

As there are other developers on this project, who implement other parts of the game,
it's crucial to use the provided function names and conform with the requirements
to have a working final product.
Also note that your git commit messages communicate your intents to your team-mates,
so make sure to write meaningful ones.

## What are you going to learn?

- Use the dictionary data structure.
- Use loops.
- Print data on console in an organized way.
- Work with files.
- Handle errors.


## Tasks

1. Write a function named `display_inventory(inventory)` that takes any possible inventory as a dictionary and displays its contents.
    - Calling the function with a non-empty dictionary argument results in displaying each key, followed by a colon, a space, the corresponding value, and a new line.
    - Calling the function with an empty dictionary returns nothing.

2. Write a function named `add_to_inventory(inventory, added_items)` that adds the contents of the `added_items` list to the `inventory` dictionary.
    - When the function is called with items that are not in the inventory, the items are added to the inventory with 1 as their initial value.
    - When the function is called with items that are in the inventory, the value of those items is increased by 1.
    - The function can handle multiple occurrences of the same item in `added_items`. In this case, the value of the item is increased by the number of occurrences.

3. Write a function named `remove_from_inventory(inventory, removed_items)` that removes the contents of the `removed_items` list from the `inventory` dictionary.
    - When the function is called with items which are in the inventory, the values of the keys matching the items are decreased by 1.
    - If any value in the dictionary becomes 0 or less after decreasing, the corresponding key is removed.
    - If the `removed_items` argument contains multiple occurences of the same item, dictionary values are decreased by the number of occurences.
    - Calling the function with a dictionary and items that are not in the inventory results in no change to the dictionary.

4. Write a function named `print_table(inventory, order)` that takes an inventory as parameter and displays it in an ordered, well-organized table with each column right-aligned.
    - Calling the function with a non-empty dictionary argument results
in displaying a two-column table with all the items, where the first
column contains the keys and the second column contains the values,
similar to the following example.

          -----------------
          item name | count
          -----------------
          gold coin |    45
              arrow |    12
              torch |     6
             dagger |     2
               rope |     1
               ruby |     1
          -----------------
    - The printing order can be set with the `order` parameter in the following way.
      * empty (by default) means the table is unordered
      * `count,desc` means the table is ordered by count (of items in the inventory) in descending order
      * `count,asc` means the table is ordered by count in ascending order

5. Write a function named `import_inventory(inventory, filename)` which can import new inventory items from a CSV file.
    - The function can handle CSV files containing items in
the `ruby,rope,ruby,gold coin,ruby,axe` format.
    - When the method is called with a file in comma separated format (such as `rope, torch, arrow`), that contains items which are not in the inventory, the items are added to the inventory with 1 as their initial value.
    - When the function is called with a CSV file containing items which are already in the inventory, the value of those items is increased by 1.
    - The function can handle if the CSV file contains multiple occurences of the same item. In that case, dictionary values are incremented by the number of occurences.
    - If not specified, the `filename` is `import_inventory.csv` by default.
    - If the file provided in the `filename` argument is not found, the `File '<filename>' not found!` error message is displayed.

6. Write a function named `export_inventory(inventory, filename)` which can export all inventory items to a CSV file.
    - Calling the function with a non-empty dictionary and a `filename` argument results in the dictionary keys being saved in a CSV format in the file.
    - If there are keys in the dictionary with values greater than 1, the key is saved in the file a number of times that equals the value.
    - If not specified, the `filename` is `export_inventory.csv` by default.
    - The file denoted in the `filename` argument is automatically created if it does not exist. The file is overwritten if it already exists.
    - If the user executing the function does not have write access in the folder where the script is executed, the `You don't have permission creating file '<filename>'!` error message is displayed.

## General requirements

None

## Hints

- Use a for loop to loop through all the keys in a dictionary.
- Use [F-strings](https://realpython.com/python-f-strings/) to print out
  variables mixed with text comfortably.
- Feel free to include any code in the main part of the program (outside of
  the functions) during development if you want to try out your functions.
  Make sure to remove these lines or protect them with an `if __name__ == "__main__":`
  [code snippet](https://docs.python.org/3/library/__main__.html) before pushing
  your code.
- Use the public tests of the project to check whether your functions work
  as intended. Run the test file with `python3 game_inventory_test.py -v` to get a
  detailed output. Note that passing all tests not necessarily means passing all
  requirements.


## Background materials

- <i class="far fa-exclamation"></i> [Working with Dictionaries and Collections](project/curriculum/materials/pages/python/working-with-dictionaries-and-more-collection-types.md)
- <i class="far fa-exclamation"></i> [Working with Strings](project/curriculum/materials/pages/python/working-with-strings-string-functions-and-manipulators.md)
- <i class="far fa-exclamation"></i> [Working with Functions](project/curriculum/materials/pages/python/working-with-functions-and-their-arguments-input-parameters-or-default-parameters.md)
- <i class="far fa-exclamation"></i> [Error handling in Python](https://realpython.com/python-exceptions/)
- <i class="far fa-exclamation"></i> [What is `if __name__ == "__main__"`??](https://thepythonguru.com/what-is-if-__name__-__main__/)
- <i class="far fa-exclamation"></i> [Sorting](project/curriculum/materials/competencies/python-data-structures/python-sorting.md.html)
- <i class="far fa-exclamation"></i> [Commit messages tutorial](https://www.youtube.com/watch?v=9Siot_y9wY8)
- <i class="far fa-book-open"></i> [Deep-dive into git commit messages](https://chris.beams.io/posts/git-commit/)
