package Queue;

import java.util.Iterator;
// Link list implementation
class Queue<Item> implements Iterable<Item>{

    // Nested class
    class Node{
        // Default constructor 
        Node(){
            this.next = null;
            this.data = null;
        }
        // 
        Node(Node next, Item data){
           this.next = next;
           this.data = data; 
        }
        private Node next;
        private Item data;
    // Gettters and setter methods
    public Node getNext(){ return this.next;}
    public Item getData(){ return this.data;}

    public void setNext(Node next){ this.next = next;}
    public void setData(Item data){this.data = data;}
    }

    
    Node tail = null;
    Node head = null;
    int size = 0;
    // Queue constructor
    // Creates an empty queue
    Queue(){
        tail = null; // points to the end of a link list
        head = tail; // points to the beggining of a link list
    }

    boolean isEmpty(){ if(size == 0){return true;} return false;}

    // Queue Methods 
    // Adding an item
    void enqeueu(Item data){

        if(size == 0){
            head = new Node(tail, data);
        }else{
         Node current = head;
         while(current.getNext() != tail){
            current = current.getNext();
         }   
         current.setNext(new Node(tail, data));
        }
        size++; // Number of items in the list increments by 1
    }
    
    // Removing an item
    Item deque(){
        if( size == 0){
            System.out.println("Qeueue is empty");
            return null;
        }
        Node tmp = head;
        head = (tmp.getNext() == tail) ? tail : tmp.getNext();
        tmp.setNext( null);
        size--;        
        return tmp.getData();
    }

    // Return Iterable object
    public Iterator<Item> iterator(){
        return new QueueIterator();
    }

    private class QueueIterator implements Iterator<Item>{
        Node current = head;
        public boolean hasNext(){
            if(current.getNext() != tail){return true;}
            return false;
        }
        public Item next(){
            current = current.getNext();
            return current.getData();
        }
        public void remove(){};
    }

    // Testing 
    public static void main(String args){
        Queue<Integer> m = new Queue<Integer>();
        System.out.println("Qeueue size:");
        System.out.print( m.size + "\n");
        // Store Items in the queue
        for(int i = 0; i < 10; i=i*2){
            System.out.println("Stored value: " + i);
            m.enqeueu(i);
        }
        System.out.println("Qeueue size:");
        System.out.print( m.size + "\n");
        System.out.println("Values in the queueu");
        for(Integer item: m){
            System.out.println(item);
        }
        System.out.println("END!");
    }
}