<script>
    import '../app.css'
  import '../prism.css'
  import { name } from '$lib/info.js'

  /** @type {import('./$types').PageData} */
  // import {URL} from '$app/stores'
  // export let data

  // import {page} from '$app/stores'
  // console.log("PAGE PAGE", $page.url.pathname)

</script>

<svelte:head>
  <title>{name}</title>
  <!-- <meta name="description" content={bio} /> -->
</svelte:head>

<div class="max-w-4xl mx-auto pr-10px pl-10px">

  <div class='float-left mx-auto'>
<img alt='about image' src='/about.png' class="max-w-50px"/>
</div>


<div class='float pl-20px'>
<p>Ello.</p><br>

<p>My name is Josh. I love learning. This site mostly hosts bits and pieces of my process - what I’m reading and scribbling etc.; as well as projects I'm working on.</p><br>

<p>By day I am a data journalist at <a href='https://www.theguardian.com/profile/josh-nicholas' target='_blank'>The Guardian</a>. Before that I covered <a href='https://theconversation.com/speaking-with-law-professor-cass-sunstein-on-why-behavioural-science-is-always-nudging-us-101074' target='_blank'>economics</a>, <a href='https://www.businessinsider.com.au/photos-inside-the-library-of-the-future-2015-12' target='_blank'>tech</a> and made <a href='https://www.thewire.org.au/about/team/alumni/' target='_blank'>podcasts and radio</a>.</p><br>

<p>This site is over a decade old and has gone through many platforms and stylistic iterations. The current version was built with <a href='https://kit.svelte.dev/' target='_blank'>Svelte</a> and a rapidly changing API could break it at any moment. Content is also being programmatically pulled from other places. As a result some links, line breaks, quotes etc., may be janky.</p><br>

<p>You can also find me on <a href='https://twitter.com/joshcnicholas' target='_blank'>Twitter</a>, <a href='https://joshnicholas.micro.blog/' target='_blank'>Micro.blog</a>, <a href='https://www.goodreads.com/joshnicholas' target='_blank'>Goodreads</a> and <a href='https://github.com/joshnicholas' target='_blank'>GitHub</a>.</p>
</div>
    
</div>

<style>
  a {
    color: #84cc16
  }
</style>
