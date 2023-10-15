class A extends Object{
    public A(){
        super();
        System.out.println("in A");
    }
    public A(int n){
        super();
        System.out.println(n);
    }
}
class B extends A{
    public B(){
        super();
        System.out.println("in B");
    }
    public B(int n){
        //super(n);
        this();
        System.out.println(n+n);
    }
}
public class ThisandSuper{
    public static void  main(String args[]){
        B obj =new B(3);
        //B obj1 =new B();
        new A();//anonymous object
    }
}
