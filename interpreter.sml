    fun compareCharLists([],[]) = true

        |compareCharLists((x::xs):char list,(l::ls):char list) = ((x = l) andalso (compareCharLists(xs,ls)))
        |compareCharLists(_,_) = false

    fun splitByFirstSpace(s: string)=
      let val temp = explode s
          fun helper(a:char list, b:char list)=
            case b of
              []=> []
              |(x::xs)=> if (Char.isSpace x) then
              let val x = implode a
                  val y = implode xs
              in
              [x,y]
              end
              else
              helper(a@[x], xs)
          in
            helper([],temp)
          end

    fun checkInthelper(l:char list)=
       case l of
         [] => false
         |(x::xs)=>
                let
                  fun helper(l:char list)=
                    case l of
                      [] => true
                      |(x::xs)=> if(Char.isDigit x) then helper(xs) else false
                in
                  if (x = #"-") then helper(xs) else
                   helper(l)
                end

    fun checkInt(l:char list, bindStack)=
        if checkName(l) then
        if checkifBound(l, bindStack) then
        let val temp = getBoundVal(l, bindStack)
        in
        checkInthelper(explode temp)
        end
        else
        false
        else
        checkInthelper(l)

    fun valInt(l:char list, bindStack)=
        if checkName(l) then
        if checkifBound(l, bindStack) then
        let val temp = getBoundVal(l, bindStack)
        in
        Int.fromString(temp)
        end
        else
        SOME (0)
        else
        Int.fromString(implode l)

    fun checkStringhelper(l:char list)=
        case l of
          [] => false
          |(x::xs)=>
                let
                  val temp = implode l
                  in
                  if (String.isPrefix "\"" temp) then
                  if (String.isSuffix "\"" temp) then
                  true else false
                  else false
                end

    fun checkString(l:char list, bindStack)=
        if checkName(l) then
        if checkifBound(l, bindStack) then
        let val temp = getBoundVal(l, bindStack)
        in
        checkStringhelper(explode temp)
        end
        else
        false
        else
        checkStringhelper(l)


    fun valString(l:char list, bindStack)=
        if checkName(l) then
        if checkifBound(l, bindStack) then
        getBoundVal(l, bindStack)
        else
        ""
        else
        (implode l)


    fun checkName(l:char list)=
        case l of
          [] => false
          |(x::xs)=>
                if (Char.isAlpha x) then
                  let fun helper(l:char list)=
                    case l of
                      [] => true
                      |(x::xs)=> if(Char.isAlphaNum x) then helper(xs) else false
                  in
                    helper(xs)
                  end
                else false

    fun checkBoolhelper(l:char list)=
        let
          val word = implode l
        in
          case word of
          ":true:" => true
          |":false:" => true
          |(some) => false
        end

    fun checkBool(l:char list, bindStack)=
        if checkName(l) then
        if checkifBound(l, bindStack) then
        let val temp = getBoundVal(l, bindStack)
        in
        checkBoolhelper(explode temp)
        end
        else
        false
        else
        checkBoolhelper(l)

    fun valBool(l:char list, bindStack)=
      let fun computeBool(entry: string)=
        case entry of
          ":true:"=> true
          |":false:"=> false
      in
        if checkName(l) then
        if checkifBound(l, bindStack) then
        computeBool(getBoundVal(l, bindStack))
        else
        false
        else
        computeBool(implode l)
      end

    fun checkifBound(l:char list, bindStack)=

      let fun helper(li)=
        case li of
          []=> false
          |((x1,x2)::xs)=> if compareCharLists(l, (explode x1)) then true
            else helper(xs)
      in
          helper(bindStack)
      end

    fun getBoundVal(l:char list, bindStack)=
        let fun helper(li)=
          case li of
            []=> ""
            |((x1,x2)::xs)=> if compareCharLists(l, (explode x1)) then x2
              else helper(xs)
        in
            helper(bindStack)
        end

    fun binOp(oper:string, stack: string list, bindStack)=

        if(checkInt(explode (List.last stack),bindStack)) then
        if(checkInt(explode (List.nth(stack, ((List.length stack) - 2))),bindStack)) then
          let
            val SOME a = valInt ((explode (List.last stack)), bindStack)
            val temp = List.take(stack, ((List.length stack) - 1))
            val SOME b = valInt ((explode (List.last temp)), bindStack)
            val temp1 = List.take(temp, ((List.length temp) - 1))
          in
            case oper of

              "add"=>
                    if ((a+b) < 0) then (temp1@["-" ^ Int.toString(~(a+b))]) else (temp1@[Int.toString((a+b))])

              |"sub"=>
                    if ((b-a) < 0) then (temp1@["-" ^ Int.toString(~(b-a))]) else (temp1@[Int.toString((b-a))])

              |"mul"=>
                    if ((a*b) < 0) then (temp1@["-" ^ Int.toString(~(a*b))]) else (temp1@[Int.toString((a*b))])

              |"div"=>
                    if (a=0) then stack@[":error:"] else
                    if ((b div a) < 0) then (temp1@["-" ^ Int.toString(~(b div a))]) else (temp1@[Int.toString((b div a))])

              |"rem"=>
                    if (a=0) then stack@[":error:"] else
                    if ((b mod a) < 0) then (temp1@["-" ^ Int.toString(~(b mod a))]) else (temp1@[Int.toString((b mod a))])

              |(some)=> stack@[":error:"]

          end
        else stack@[":error:"]
        else stack@[":error:"]




        fun boolOp(oper:string, stack: string list, bindStack)=
            if(checkBool(explode (List.last stack),bindStack)) then
            if(checkBool(explode (List.nth(stack, ((List.length stack) - 2))),bindStack)) then
              let
                val a = valBool(explode(List.last stack), bindStack)
                val temp = List.take(stack, ((List.length stack) - 1))
                val b = valBool(explode(List.last temp), bindStack)
                val temp1 = List.take(temp, ((List.length temp) - 1))

              in
                case oper of

                  "and"=>
                        if ((a andalso b)) then (temp1@[":true:"]) else (temp1@[":false:"])

                  |"or"=>
                        if ((a orelse b)) then (temp1@[":true:"]) else (temp1@[":false:"])


                  |(some)=> stack@[":error:"]

              end
            else stack@[":error:"]
            else stack@[":error:"]

        fun notOp(stack: string list, bindStack)=
            if(checkBool(explode (List.last stack),bindStack)) then
              let
                val a = valBool(explode(List.last stack),bindStack)
                val temp = List.take(stack, ((List.length stack) - 1))

              in
                if (not a) then (temp@[":true:"]) else (temp@[":false:"])

              end
            else stack@[":error:"]

        fun ifOp(stack: string list, bindStack)=
            if(checkBool(explode (List.nth(stack, ((List.length stack) - 3))),bindStack)) then
            let
              val a = (List.last stack)
              val temp = List.take(stack, ((List.length stack) - 1))
              val b = (List.last temp)
              val temp1 = List.take(temp, ((List.length temp) - 1))
              val c = valBool(explode(List.last temp1),bindStack)
              val temp2 = List.take(temp1, ((List.length temp1) - 1))
            in
              if c then temp2@[b] else temp2@[a]
            end
            else stack@[":error:"]

        fun compareOp(oper:string, stack: string list, bindStack)=
            if(checkInt(explode (List.last stack),bindStack)) then
            if(checkInt(explode (List.nth(stack, ((List.length stack) - 2))),bindStack)) then
              let
                val SOME a = valInt(explode(List.last stack),bindStack)
                val temp = List.take(stack, ((List.length stack) - 1))
                val SOME b = valInt(explode(List.last temp),bindStack)
                val temp1 = List.take(temp, ((List.length temp) - 1))
              in
                case oper of

                  "equal"=>
                        if (a = b) then (temp1@[":true:"]) else (temp1@[":false:"])

                  |"lessThan"=>
                        if (b < a) then (temp1@[":true:"]) else (temp1@[":false:"])

                  |(some)=> stack@[":error:"]

              end
            else stack@[":error:"]
            else stack@[":error:"]


      fun neg(stack:string list, bindStack)=
          if(checkInt(explode (List.last stack),bindStack)) then
            let
              val SOME a = (valInt(explode(List.last stack),bindStack))
              val temp = List.take(stack, ((List.length stack) - 1))
            in
              if ((~a) < 0) then (temp@["-" ^ Int.toString((a))]) else (temp@[Int.toString((~a))])
            end
          else stack@[":error:"]

    fun catOp(stack:string list, bindStack)=
        if(checkString(explode (List.last stack),bindStack)) then
        if(checkString(explode (List.nth(stack, ((List.length stack) - 2))),bindStack)) then
          let
            val a = valString(explode (List.last stack), bindStack)
            val temp = List.take(stack, ((List.length stack) - 1))
            val b = valString(explode (List.last temp), bindStack)
            val temp1 = List.take(temp, ((List.length temp) - 1))
          in
            temp1@[(String.substring(b, 0, ((String.size b) - 1)))^(String.substring(a, 1, ((String.size a) - 1)))]
          end
        else stack@[":error:"]
        else stack@[":error:"]

    fun swap(stack:string list)=
        let
          val a = (List.last stack)
          val temp = List.take(stack, ((List.length stack) - 1))
          val b = (List.last temp)
          val temp1 = List.take(temp, ((List.length temp) - 1))
        in
          temp1@[a]@[b]
        end

    fun bindOp(stack:string list, bindStack)=
        if(checkName(explode (List.nth(stack, ((List.length stack) - 2))))) then
        case (List.last stack) of
        ":error:"=> ((stack@[":error:"]),bindStack)
        |(a)=>
          if checkName(explode a) then
          if checkifBound(explode a, bindStack) then
          let
            val a = getBoundVal(explode(List.last stack),bindStack)
            val temp = List.take(stack, ((List.length stack) - 1))
            val b = (List.last temp)
            val temp1 = List.take(temp, ((List.length temp) - 1))
          in
            ((temp1@[":unit:"]),(bindStack@[(b,a)]))
          end
          else
          ((stack@[":error:"]),bindStack)
          else
          let
            val a = (List.last stack)
            val temp = List.take(stack, ((List.length stack) - 1))
            val b = (List.last temp)
            val temp1 = List.take(temp, ((List.length temp) - 1))
          in
            ((temp1@[":unit:"]),(bindStack@[(b,a)]))
          end
        else ((stack@[":error:"]),bindStack)

    fun computeVal(w:string)=
        case w of
            ":unit:"=>[":unit:"]
            |(some)=>
                let
                  val cList = explode w
                in
                  (case cList of
                  [] => [":error:"]
                  |(x::xs) =>
                        case x of
                        #"-" =>
                              (case xs of
                              [] => [":error:"]
                              |(x::xs) => if (x = #"0") then ["0"] else
                                          if checkInthelper(cList) then [some] else [":error:"]
                              )
                        |(any) => if checkInthelper(cList) then [some] else
                                  if checkName(cList) then [some] else
                                  if checkBoolhelper(cList) then [some] else
                                  if checkStringhelper(cList) then [some] else [":error:"]

                  )
                end




    fun interpreter(inFile : string, outFile : string)=
      let
          val ins = TextIO.openIn inFile
          val outs = TextIO.openOut outFile
          val line = TextIO.inputLine ins
          val outputStack = []
          val bindVals = []

          fun print([]) = ""
            | print(a::b) =

              if checkStringhelper(explode (a)) then
              (TextIO.output(outs, (String.substring(a, 1, ((String.size a) - 2)))^"\n"); print(b))
              else
              (TextIO.output(outs, a^"\n"); print(b))


          fun helper(stack: string list, inList: string, bindStack)=
            let
              val f = splitByFirstSpace(inList)
              val word1 = List.hd(f)
            in
              case word1 of
                "push" =>
                  let
                    val expression = String.substring((List.nth(f, 1)), 0, ((String.size(List.nth(f, 1))-1)))
                    val value = computeVal(expression)

                  in
                    ((stack@value), bindStack)
                  end

                |"pop" =>
                    let
                      val length = List.length stack
                    in
                      if (length = 0) then (stack@[":error:"], bindStack) else
                      (List.take(stack, (length -1)), bindStack)
                    end

                |("add"|"sub"|"mul"|"div"|"rem") =>
                    let
                      val length = List.length stack
                    in
                      if (length < 2) then (stack@[":error:"], bindStack) else
                      (binOp(word1,stack, bindStack), bindStack)
                    end

                |"neg" =>
                    let
                      val length = List.length stack
                    in
                      if (length = 0) then (stack@[":error:"], bindStack) else
                      (neg(stack,bindStack), bindStack)
                    end

                |"swap"=>
                    let
                      val length = List.length stack
                    in
                      if (length < 2) then (stack@[":error:"], bindStack) else
                      (swap(stack), bindStack)
                    end

                |("and"|"or")=>
                    let
                      val length = List.length stack
                    in
                      if (length < 2) then (stack@[":error:"], bindStack) else
                      (boolOp(word1,stack,bindStack), bindStack)
                    end

                |"not" =>
                    let
                      val length = List.length stack
                    in
                      if (length = 0) then (stack@[":error:"], bindStack) else
                      (notOp(stack,bindStack), bindStack)
                    end

                |"if" =>
                    let
                      val length = List.length stack
                    in
                      if (length < 3) then (stack@[":error:"], bindStack) else
                      (ifOp(stack,bindStack), bindStack)
                    end

                |("equal"|"lessThan") =>
                    let
                      val length = List.length stack
                    in
                      if (length < 2) then (stack@[":error:"], bindStack) else
                      (compareOp(word1,stack,bindStack), bindStack)
                    end

                |"cat" =>
                    let
                      val length = List.length stack
                    in
                      if (length < 2) then (stack@[":error:"], bindStack) else
                      (catOp(stack, bindStack), bindStack)
                    end

                |"bind" =>
                  let
                    val length = List.length stack
                  in
                    if (length < 2) then (stack@[":error:"], bindStack) else
                    bindOp(stack, bindStack)
                  end

                |"quit" =>
                    let
                      val temp = List.rev stack
                    in
                      (print(temp);([],[]))
                    end

                |(some) =>
                  (stack@[":error:"], bindStack)
              end


          fun readLine(oStack:string list, bstack, line : string option) =
            case line of
                NONE => (TextIO.closeIn ins; TextIO.closeOut outs)

               | SOME(k) =>
                     let
                       val temp = helper(oStack, k, bstack)
                     in
                      (readLine((#1temp),(#2temp),(TextIO.inputLine ins)))
                     end
        in
          readLine(outputStack,bindVals, line)
        end




(* val it = interpreter("input.txt","output.txt");
*)
