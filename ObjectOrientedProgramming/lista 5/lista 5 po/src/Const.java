public class Const extends Expression
{
    private int value;

    public Const(int value)
    {
        this.value = value;
    }
    public Expression pochodna()
    {
        this.value = 0;
        return this;
    }

    public int evaluate()
    {
        return value;
    }

    public String toString()
    {
        return Integer.toString(value);
    }
}