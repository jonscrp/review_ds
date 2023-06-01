package Queue;

// Link list implementation
class Queue<Item>{

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
        Node tail = null; // points to the end of a link list
        Node head = tail; // points to the beggining of a link list
    }

    boolean isEmpty(){ if(size == 0){return true;} return false;}

    // Queue Methods 
    void enqeueu(Item data){

        // First attempt
        // The issue of this implementation is that to deque I would have to traverse 
        // to the tail inorder to retrieve the last element. This will take O(n) time 

        // add first item
        /* 
        if(size == 0){
            head = new Node(tail, data);
        } else{
            Node current = head;
            while(current.getNext() != null){
                current = current.getNext();  
            }
            current.setNext(new Node(tail, data));
        }
        */

        // Second attempt 
        // This approach is better than the previous one since it add a new element to the beginning
        // of the link list which allows us to deque(remove the element at the top) elements from the
        // beginning of the link list instead of having to travese through the entire LL as the previous approach did. 
        // this take O(1) 
        if(size == 0){
            head = new Node(tail, data);
        }else {
            Node tmp = head; // top element
            head = new Node(tmp.getNext(), data); // add new element and set as the "head"
        }
        size++; // Number of items in the list increments by 1
    }
    
    Item deque(){

        return 
    }




    // Testing 
    public static void main(String args){


    }


}