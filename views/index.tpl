<html>
    <body>
        <h1>Hello {{user}}!</h1>
        <ul>
            % for thing in things:
              <li>thing</li>
            % end
        </ul>
    </body>
</html>
