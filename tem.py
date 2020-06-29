html = b"""
<html>
    <body>
        <form action="">
             input number =
            a = <input type="number" name="a"> <br><br>
            b = <input type="number" name="b">
            <input type="submit">
        </form>
        sum = %(a+b)d <br><br>
        mul = %(a*b)d
    </body>
</html>

