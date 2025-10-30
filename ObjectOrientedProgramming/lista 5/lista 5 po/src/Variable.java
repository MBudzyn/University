public class Variable extends Expression
{
    private String name;
    private int value;

    public Variable(String name)
    {
        this.name = name;
    }

    public int evaluate()
    {
        return value;
    }
    public Expression pochodna()
    {
        this.name = "1";
        this.value = 1;
        return this;
    }
    public void setValue(int value)
    {
        this.value = value;
    }

    public String toString()
    {
        return name;
    }
}