import teal_algos.factorielle as f
import teal_algos.matrixproduct as mp
import teal_algos.rowcolsum as rc
import sys
print(
     "***********"   "\t****************\t"     "*******************\t"      "*******\n"
     "***********"   "\t******           \t"     "*******************\t"      "******\n"
     "   ***    "    "\t*****           \t"      "******    ********* \t"     "******\n"
     "   ***    "    "\t*****************\t"     "*******************\t"      "******\n"
     "   ***    "    "\t******           \t"     "*******************\t"      "*****************\n"
     "   ***    "    "\t******           \t"     "******       ******\t"      "*****************\n"
     "   ***    "    "\t*****************\t"     "******       ******\t"      "*****************\n"
    )
print("An opensource test app by Taneristique")
def menu():
    Menu="Menu\n1.Merge Sort\n2.Bubble Sort\n3.Factorielle\n4.Fibonacci\n5.Find Matrix Product\n6.Find Rowsum And Colsum Of A Matrix\n7.Play the game 'Guess A Number\n8.Exit'"
    print(Menu)
    chose=int(input())
    action_list={1:mergeSort,2:bubbleSort,3:factorielle,4:fibonacci,5:product,6:sumofrowandcol,7:game} if chose!=0 else sys.exit()
    action_list[chose]()
def game():
    import teal_algos.guessnumber
    menu()
def fibonacci():
    import teal_algos.fibonacci
    menu()
def mergeSort():
    import teal_algos.merge
    menu()
def bubbleSort():
    import teal_algos.bubble
    menu()
def factorielle():
    print(f.factorial(int(input("give a number"))))
    menu()
def product():
    mp.mproduct(int(input("number of rows\n")),int(input("number of cols\n")))
    menu()
def sumofrowandcol():
    rc.RowColSum(int(input("Dimension of matrix, please  give an integer\n")))
    menu()


if __name__== '__main__':
    menu()