# acme-widget-pos
Interactive CLI based Proof of concept for a POS system

Assumptions:
- Unlimited Inventory for all the widgets
- Global currency used is USD
- Final Values rounded off to 2 decimal places


Can be improved:
- Current design for delivery charges is based on static values as per the assesment, it can be improved by creating base interface and extending multiple delivery strategies as per requirements.
- Yaml/ Config files can be utilised for instantiating catalogue and also specifing the exact widget for the given offer type.
- A chaining design based implementation can be done inorder to support and choose the best discount from multiple offers.



Steps to execute:
clone repo and run main.py from terminal/IDE/shell


Screenshots for reference:

<img width="725" alt="Screenshot 2022-09-24 at 7 13 31 PM" src="https://user-images.githubusercontent.com/75936788/192101365-c7fc9376-b230-4a4c-a942-861eb9b81a92.png">

<img width="1094" alt="Screenshot 2022-09-24 at 7 14 12 PM" src="https://user-images.githubusercontent.com/75936788/192101427-c4238f19-5549-4904-bb3f-65acb593aafa.png">

<img width="868" alt="Screenshot 2022-09-24 at 7 14 22 PM" src="https://user-images.githubusercontent.com/75936788/192101391-14830508-343c-4cb4-8ec8-56779760f74e.png">


Running tests:
run runner.py from terminal/IDE/shell

<img width="906" alt="Screenshot 2022-09-25 at 12 32 38 AM" src="https://user-images.githubusercontent.com/75936788/192114494-33266d99-0380-4a1d-a85a-c3b5f4144f0d.png">
