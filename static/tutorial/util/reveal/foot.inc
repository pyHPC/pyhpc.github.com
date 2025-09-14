        <script src="lib/js/head.min.js"></script>
        <script src="js/reveal.min.js"></script>
        <script type="text/javascript" src="mathjax/MathJax.js?config=default"></script>
        
        <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.6.2/jquery.min.js"></script>

        <script>
            Reveal.initialize({
                controls: true,
                progress: true,
                history: true,
                center: false,
                rollingLinks: false,
                transition: 'none',
                width: 1024,
                height: 768,


                // Optional libraries used to extend on reveal.js
                dependencies: [
                    { src: 'lib/js/classList.js', condition: function() { return !document.body.classList; } },
                    { src: 'plugin/highlight/highlight.js', async: true, callback: function() { hljs.initHighlightingOnLoad(); } },
                    { src: 'plugin/zoom-js/zoom.js', async: true, condition: function() { return !!document.body.classList; } },
                    { src: 'plugin/notes/notes.js', async: true, condition: function() { return !!document.body.classList; } },
                    { src: 'plugin/markdown/showdown.js', condition: function() { return !!document.querySelector( '[data-markdown]' ); } },
                    { src: 'plugin/markdown/markdown.js', condition: function() { return !!document.querySelector( '[data-markdown]' ); } },
                ]
            });

        </script>
    </body>
</html>
