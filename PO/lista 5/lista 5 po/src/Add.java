public class Add extends Expression
{
    private Expression left;
    private Expression right;

    public Add(Expression left, Expression right)
    {
        this.left = left;
        this.right = right;
    }

    public int evaluate()
    {
        return left.evaluate() + right.evaluate();
    }
    public Expression pochodna()
    {
        Add zmienna = new Add(left.pochodna(),right.pochodna());
        return zmienna;
    }

    public String toString()
    {
        return "(" + left.toString() + " + " + right.toString() + ")";
    }
}