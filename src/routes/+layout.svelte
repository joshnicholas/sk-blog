<script>
  import '../app.css'
  import '../prism.css'
  import MoonIcon from 'heroicons-svelte/solid/MoonIcon.svelte'
  import SunIcon from 'heroicons-svelte/solid/SunIcon.svelte'
  import { browser } from '$app/environment'
  import { name } from '$lib/info'

  // import {page} from '$app/stores'
  // // let pathos = $page.url.pathname
  // console.log("PAGE PAGE", $page.url.pathname)

  // export let pathos = $page.url.pathname

    import Navvy from '$lib/components/nav.svelte'
    // import Footy from '$lib/components/footer.svelte'

  // import nav from ''

  let isDarkMode = browser ? Boolean(document.documentElement.classList.contains('dark')) : true

  function disableTransitionsTemporarily() {
    document.documentElement.classList.add('[&_*]:!transition-none')
    window.setTimeout(() => {
      document.documentElement.classList.remove('[&_*]:!transition-none')
    }, 0)
  }
</script>

<Navvy/>

<div class=" max-w-4xl mx-auto pl-10 pr-10 pt-10">

<slot />

</div>

<!-- <Footy/> -->