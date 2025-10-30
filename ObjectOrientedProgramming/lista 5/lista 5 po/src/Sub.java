public class Sub extends Expression
{
    private Expression left;
    private Expression right;
    public Sub(Expression left, Expression right)
    {
        this.left = left;
        this.right = right;
    }
    public int evaluate()
    {
        return left.evaluate() - right.evaluate();
    }
    public Expression pochodna()
    {
        Sub t = new Sub(left.pochodna(),right.pochodna());
        return t;
    }

    public String toString()
    {
        return "(" + left.toString() + " - " + right.toString() + ")";
    }
}