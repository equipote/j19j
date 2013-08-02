Código personalizado para realizar búsquedas dentro del dominio DemocraciaRealYa

`Google Custom Search Engine <http://www.google.com/cse/>`_

.. code-block:: javascript
    :linenos:

    <script>
        (function() {
            var cx = '004640732731469104663:ay2rocw8so8';
            var gcse = document.createElement('script');
            gcse.type = 'text/javascript';
            gcse.async = true;
            gcse.src = (document.location.protocol == 'https:' ? 'https:' : 'http:') +
                '//www.google.com/cse/cse.js?cx=' + cx;
            var s = document.getElementsByTagName('script')[0];
            s.parentNode.insertBefore(gcse, s);
        })();
    </script>
    <gcse:search></gcse:search>

