function Tree(val, left, right) 
    {
        this.left = left;
        this.right = right;
        this.val = val;

    }
Tree.prototype[Symbol.iterator] = function*() 
    {
        var tab = [this]
        while (tab.length !=0 ){
            var pom = tab[0]
            if (tab[0] == undefined)
                {tab.splice(0,1)}
            else
            {
            yield tab[0].val
            tab.splice(0,1)
            tab.splice(tab.length,0,pom.right)
            tab.splice(tab.length,0,pom.left)
            }
    }
    }

    var root = new Tree( 1,
    new Tree( 2, new Tree( 3 ) ), new Tree( 4 ));

    for ( var e of root ) 
    {
        console.log( e );
    }
   // 1 2 3 4
