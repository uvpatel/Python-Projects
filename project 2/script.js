
        window.addEventListener('scroll', function() {
            let elements = document.querySelectorAll('.resume');
            let windowHeight = window.innerHeight;

            elements.forEach(function(element) {
                let positionFromTop = element.getBoundingClientRect().top;

                if (positionFromTop - windowHeight <= 0) {
                    element.classList.add('show');
                }
            });
        });

