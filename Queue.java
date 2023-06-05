// Queue implementation
import java.util.Iterator;

class Queue<Item> implements Iterable<Item> {

    private class Node {
        Item data;
        Node next;
    }
    Node tail;
    Node head;
    int size = 0;
    // Queue constructor
    // Creates an empty queue
    Queue(){
        tail = null; // points to the first element of the LL
        head = null; // points to the last elments of the LL
    }

    boolean isEmpty(){ if(size == 0){return true;} return false;}
    // Queue Methods 
    // Adding an item
    void enqeueu(Item data){
        Node oldtail = tail;
        tail = new Node();
        tail.next = null;
        tail.data = data;
        if(isEmpty()){
            head = tail;
        }else{
            oldtail.next = tail;
        }
        size++; // Number of items in the list increments by 1
    }
    
    // Removing an item
    Item deque(){
        if( size == 0){
            System.out.println("Qeueue is empty");
            return null;
        }
        Item element = head.data;
        head = head.next;
        size--; 
        if(isEmpty()){ tail = null;}       
        return element;
    }

    // Iterable
    public Iterator<Item> iterator(){
        return new ListIterator();
    }

    private class ListIterator implements Iterator<Item>{
        private Node current = head;

        public boolean hasNext() {
            return current != null;
        }

        public Item next() {
            Item i = (Item)current.data;
            current = current.next;
            return i ;
        }
        public void remove(){}
    }

    public int size(){return size;}


    // Testing 
    public static void main(String []args){
        Queue<Integer> m = new Queue<Integer>();
        System.out.println("Qeueue size:");
        System.out.print( m.size + "\n");
        // Store Items in the queue
        for(int i = 0; i < 10; i++){
            System.out.println("Stored value: " + i);
            m.enqeueu(i);
        }
        System.out.println("Qeueue size:");
        System.out.print( m.size + "\n");
        System.out.println("Values in the queueu");
        for(Integer p: m){
            System.out.println(p);
        }
        System.out.println("END!");
    }
}