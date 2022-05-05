
function ListNode(val, next) {
     this.val = (val===undefined ? 0 : val)
     this.next = (next===undefined ? null : next)
 }


var reverseList = function(head) {
    var node = head;
    var prev = null;

    while(node){
        var swap = node.next;
        node.next = prev;
        prev = node;
        node = swap;
    }
    return prev;
    
};


var node1 = new ListNode(1, new ListNode(2, new ListNode(3, null)));
console.log(reverseList(node1));