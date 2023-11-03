<script>
    // import NewGallery from '$lib/components/newGallery.svelte'
  // import ScribblesList from '$lib/components/ScribblesList.svelte';


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

<div class="max-w-3xl mx-auto">

  <div class='float-left mx-auto pr-4'>
<!-- <img alt='about image' src='/about.png' class="max-w-50px rounded"/> -->
<img alt='about image' src='/new_about.jpg' class="pb-2 max-h-[15rem] mx-auto rounded"/>


</div>


<div class='float pl-20px'>
  <br>
<p>Ello.</p><br>
<!-- , <a href='https://joshnicholas.com/projects'>projects</a> I'm working on -->
<p>My name is Josh. I love learning. </p><br>
  
<p>This site hosts what would otherwise be more ephemeral - what I’m <a href='https://joshnicholas.com/words'>reading</a> and <a href='https://joshnicholas.com/scribbles'>scribbling</a> etc.</p><br>

<p>I am a data journalist at <a rel="noreferrer" href='https://www.theguardian.com/profile/josh-nicholas' target='_blank'>The Guardian</a>. Before that I covered <a href='https://theconversation.com/speaking-with-law-professor-cass-sunstein-on-why-behavioural-science-is-always-nudging-us-101074' rel="noreferrer" target='_blank'>economics</a> and technology, and made <a href='https://www.thewire.org.au/about/team/alumni/' rel="noreferrer" target='_blank'>podcasts and radio</a>.</p><br>

<!-- <p>This site was built with an earlier version of <a rel="noreferrer" href='https://github.com/joshnicholas/sk-blog' target='_blank'>Sveltekit</a>. An API change could break it any day now. Content is also being programmatically pulled from other places. As a result some links, line breaks, quotes etc., may be janky.</p><br> -->

<p>I post more regularly on <a rel="me" href='https://micro.blog/JoshNicholas' target='_blank'>micro.blog</a>. You can follow me on <a href='https://micro.blog/JoshNicholas?remote_follow=1' target='_blank'>mastodon</a>.<br>
</div>


</div>

<style>
  a {
    color: #84cc16
  }
</style>
