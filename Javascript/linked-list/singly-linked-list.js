
 // Definition for singly-linked list.
 function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
   }
   
  /**
   * @param {ListNode} l1
   * @param {ListNode} l2
   * @return {ListNode}
   */
  var addTwoNumbers = function(l1, l2) {
      let linkedList, nextNode, remainder=0;
      do {
        let l1Val = l1 ? l1.val : null;
        let l2Val = l2 ? l2.val : null;
        const sum = l1Val + l2Val + remainder;
        const val = sum % 10;
        remainder = Math.trunc(sum/10);
  
        if (nextNode === undefined){
          linkedList = new ListNode(val);
          nextNode = linkedList;
        } else {
          nextNode.next = new ListNode(val);
          nextNode = nextNode.next;
        }
  
        l1 = l1 ? l1.next : null;
        l2 = l2 ? l2.next : null;
      } while (l1 || l2);
  
      if (remainder) {
        nextNode.next = new ListNode(1);
      }
  
      return linkedList;
  };
  