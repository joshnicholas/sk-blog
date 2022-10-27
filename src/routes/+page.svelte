<script>
  // import ArrowRightIcon from '$lib/components/ArrowRightIcon.svelte'
  // import PostsList from '$lib/components/WordsList.svelte'
  import SocialLinks from '$lib/components/SocialLinks.svelte'
  import { avatar, bio, name } from '$lib/info.js'

  /** @type {import('./$types').PageData} */
  // export let data

</script>

<svelte:head>
  <title>{name}</title>
  <meta name="description" content={bio} />
</svelte:head>

<div class="flex flex-col flex-grow gap-8 pb-16">
  <!-- bio -->

  <section class="flex flex-col flex-grow w-full max-w-2xl">

    <p>Ello</p>

<p>My name is Josh. I love learning. This site is mostly just bits and pieces of my process - what I’m reading, thinking; my photos and scribbles.</p>

<p>By day I am a data journalist at The Guardian. Before that I covered economics, tech and made some radio for other outlets.</p>

<p>This site is over a decade old and has gone through many platforms and stylistic iterations. A lot of content is also being programmatically pulled from other places. Some links, line breaks, quotes etc., may be janky.</p>

<p>You can also find me on Twitter, Micro.blog, Goodreads and GitHub.</p>
    
  </section>
</div>

