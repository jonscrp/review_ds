import java.util.Iterator;

public class Stack<Item> implements Iterable<Item> {
    private class Node {
        Item data;
        Node next;
    }

    
    int size = 0;
    Node head;
    Node tail;

    // Constructor
    // Empty Stack
    Stack(){
       head = null;
       tail = null; 
    }

    public void push(Item data){
        Node oldhead = head;
        head = new Node();
        head.data = data;
        head.next = oldhead;
        size++;
    }

    public Item pop(){
        if(size == 0){
            System.out.println("Stack is empty");
            return null;
        }
        Item item = head.data;
        head = head.next;
        size--;
        return item;
    }

    public Iterator<Item> iterator(){
        return new ListIterator();
    }

    private class ListIterator implements Iterator<Item>{
        private Node current = head;

        public boolean hasNext() {
            return current != null;
        }

        public Item next() {
            Item i = current.data;
            current = current.next;
            return i ;
        }
        public void remove(){}
    }

    public int size(){return size;}

    public static void main(String []args){
        Stack<Integer> m = new Stack<Integer>();
        System.out.println("Stack size:");
        System.out.print( m.size + "\n");
        // Store Items in the queue
        for(int i = 0; i < 10; i++){
            System.out.println("Stored value: " + i);
            m.push(i);
        }
        System.out.println("Stack size:");
        System.out.print( m.size + "\n");
        System.out.println("Values in the stack");
        for(Integer p: m){
            System.out.println(p);
        }       

    }
}

