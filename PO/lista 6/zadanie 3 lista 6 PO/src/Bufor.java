import java.io.Serializable;

public class Bufor<T> implements Serializable{
    private T[] buffer;
    private int head;
    private int tail;
    private int size;
    public int maxsize;

    public Bufor(int rozmiarbuffora) {
        buffer = (T[]) new Object[rozmiarbuffora];
        head = 0;
        tail = 0;
        size = 0;
        maxsize = rozmiarbuffora;
    }

    public synchronized void add(T item)
    {

        buffer[head] = item;
        head = (head + 1) % buffer.length;
        size++;
    }

    public synchronized T zwroc()  {

        T item = buffer[tail];
        tail = (tail + 1) % buffer.length;
        size--;
        return item;
    }

    public synchronized boolean jestpelny() {
        return size == buffer.length;
    }

    public synchronized boolean jestpusty() {
        return size == 0;
    }

    public synchronized int rozmiar() {
        return maxsize;
    }
}

