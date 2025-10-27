/*
Mateusz Budzyński
Lista 5 zadania 2 i 4
 */
public class Main
{
    public static void main(String[] args)
    {

        Variable x = new Variable("x");
        x.setValue(3);
        Variable y = new Variable("y");
        y.setValue(100);
        Variable z = new Variable("z");
        z.setValue(42);

        Expression expr1 = new Add(new Const(4), x);
        Expression expr2 =new Sub(new Sub (new Add(z, new Const(17)), new Const(140)) , new Sub (new Add(new Const(2343), z), z) );
        Expression expr3 =new Sub(new Sub (new Add(new Const(23), y), new Const(10)) , new Add(new Const(4), y));


        System.out.println(expr1.toString() + " = " + expr1.evaluate());
        expr1.pochodna();
        System.out.println(expr1.toString() + " = " + expr1.evaluate());
        System.out.println();

        System.out.println(expr2.toString() + " = " + expr2.evaluate());
        expr2.pochodna();
        System.out.println(expr2.toString() + " = " + expr2.evaluate());
        System.out.println();

        System.out.println(expr3.toString() + " = " + expr3.evaluate());
        expr3.pochodna();
        System.out.println(expr3.toString() + " = " + expr3.evaluate());
        System.out.println();


    }
}
