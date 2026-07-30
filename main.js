/* RXD Cloud Consulting — progressive enhancement only.
   Everything on the page works without this file: the contact form falls back to a
   normal POST, the nav falls back to a native <details> disclosure, and the copy
   button is the only element that disappears (the address stays visible either way). */

(function () {
  'use strict';

  /* ---- Conversion tracking -------------------------------------------------
     Cloudflare Web Analytics has no custom-event API. Its beacon does record
     history.pushState navigations when "spa": true, so a conversion is recorded
     as a virtual pageview under /goal/<name> and the real URL is restored
     immediately afterwards. Read these as pageviews on /goal/* in the dashboard. */
  function trackGoal(name) {
    if (!name || !window.history || !history.pushState) return;
    var here = location.pathname + location.search + location.hash;
    try {
      history.pushState({}, '', '/goal/' + name);
      history.replaceState({}, '', here);
    } catch (e) {
      /* Cross-origin or file:// — tracking is not worth breaking a click over. */
    }
  }

  document.addEventListener('click', function (event) {
    var el = event.target.closest('[data-goal]');
    if (el) trackGoal(el.getAttribute('data-goal'));
  });

  /* ---- Mobile nav ----------------------------------------------------------
     Close the disclosure after a jump, otherwise the open panel covers the
     section the user just navigated to. */
  var navMenu = document.querySelector('.nav-menu');
  if (navMenu) {
    navMenu.addEventListener('click', function (event) {
      if (event.target.closest('.nav-links a')) navMenu.removeAttribute('open');
    });
    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape' && navMenu.hasAttribute('open')) {
        navMenu.removeAttribute('open');
        var toggle = navMenu.querySelector('summary');
        if (toggle) toggle.focus();
      }
    });
  }

  /* ---- Copy-to-clipboard for the email address ---------------------------- */
  document.querySelectorAll('.copy-btn').forEach(function (btn) {
    if (!navigator.clipboard) {
      btn.remove();
      return;
    }
    btn.addEventListener('click', function () {
      navigator.clipboard.writeText(btn.dataset.copy).then(function () {
        var original = btn.textContent;
        btn.textContent = 'Copied';
        btn.classList.add('is-copied');
        setTimeout(function () {
          btn.textContent = original;
          btn.classList.remove('is-copied');
        }, 2000);
      });
    });
  });

  /* ---- Contact form -------------------------------------------------------- */
  var form = document.getElementById('contact-form');
  var status = document.getElementById('form-status');

  if (form && status && window.fetch) {
    form.addEventListener('submit', function (event) {
      event.preventDefault();

      var button = form.querySelector('button[type="submit"]');
      button.disabled = true;
      status.className = 'form-status is-pending';
      status.textContent = 'Sending…';

      fetch(form.action, {
        method: 'POST',
        headers: { Accept: 'application/json' },
        body: new FormData(form)
      })
        .then(function (response) {
          return response.json().catch(function () {
            return { success: response.ok };
          });
        })
        .then(function (data) {
          if (!data.success) throw new Error(data.message || 'Submission failed');
          form.reset();
          status.className = 'form-status is-success';
          status.textContent = 'Thanks — your message is on its way. I’ll reply within one business day.';
          trackGoal('contact-form');
        })
        .catch(function () {
          status.className = 'form-status is-error';
          status.innerHTML =
            'Something went wrong sending that. Please email ' +
            '<a href="mailto:rscloudsolutions@gmail.com">rscloudsolutions@gmail.com</a> directly.';
        })
        .then(function () {
          button.disabled = false;
        });
    });
  }
})();
