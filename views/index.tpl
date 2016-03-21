<html>
    <head>
        <title>Index</title>
    </head>
    <body>
        <h1>Hello {{user}}!</h1>
        <ul>
            % for thing in things:
              <li>thing</li>
            % end
        </ul>

        <form action="/favourite-number" method="post">
            <input name="number" type="text"/>
            <button type="submit">Submit !</button>
        </form>
    </body>
</html>
