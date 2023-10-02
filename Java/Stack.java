import java.util.*;
//Stack program

class stack {
    int stck[] = new int[10];
    double stack[] = new double[10];
    int tos, toss;

    stack() {
        tos = -1;
        toss = -1;
    }

    void push(int data) {
        // overflow:
        if (tos == stck.length - 1) {
            System.out.println("Overflow");
        } 
        else
            stck[++tos] = data;
    }

    void push(double data) {
        // overflow:
        if (toss == stack.length - 1) {
            System.out.println("Overflow");
        } 
        else
            stack[++toss] = data;
    }

    double pop() {
        // underflow:
        if (toss == -1) {
            System.out.println("underflow");
        } 
        else
            return stack[toss--];

        return -1.00;
    }

    int pops() {
        // underflow:
        if (tos == -1) {
            System.out.println("underflow");
        } 
        else
            return stck[tos--];

        return -1;
    }

    void display() {
        if (tos >= 0)
            for (int i = 0; i <= tos; i++)
                System.out.print(" " + stck[i]);
        System.out.println();
    }

    void displays() {
        if (toss >= 0)
            for (int i = 0; i <= toss; i++)
                System.out.print(" " + stack[i]);
        System.out.println();
    }
}

class Main {
    public static void main(String args[]) {
        stack st1 = new stack();

        boolean more = true;
        int data;
        double datas;

        Scanner sc = new Scanner(System.in);
        int choice;

        while (more) {
            System.out.println("1.push(DATA) in integer.");
            System.out.println("2.push(DATA) in Double.");
            System.out.println("3.pop() integer data .");
            System.out.println("4.pop() double data .");
            System.out.println("5.display Integer Stack().");
            System.out.println("6.display Double Stack().");
            System.out.println("7.Stop.");
            System.out.println("Enter your choice:");
            choice = sc.nextInt();

            switch (choice) {
                case 1:
                    System.out.println("Enter data.");

                    data = sc.nextInt();
                    st1.push(data);

                    break;

                case 2:
                    System.out.println("Enter data.");
                    datas = sc.nextDouble();
                    st1.push(datas);

                    break;

                case 3:
                    System.out.println("Popped data= " + st1.pops());
                    break;

                case 4:
                    System.out.println("Popped data= " + st1.pop());
                    break;

                case 5:
                    st1.display();
                    break;

                case 6:
                    st1.displays();
                    break;

                case 7:
                    more = false;

            }

        }
        sc.close();
    }
}
public class Stack {
    
}
