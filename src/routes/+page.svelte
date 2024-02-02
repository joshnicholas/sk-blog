<script>
    // import NewGallery from '$lib/components/newGallery.svelte'
  // import ScribblesList from '$lib/components/ScribblesList.svelte';

  import PostsList from '$lib/components/ScribblesList.svelte'
  let stem = 'scribbles'

    import '../app.css'
  import '../prism.css'
  import { name } from '$lib/info.js'

  /** @type {import('./$types').PageData} */
  // import {URL} from '$app/stores'
  // export let data

  // import {page} from '$app/stores'
  // console.log("PAGE PAGE", $page.url.pathname)


// let selected = [
//   {"Title": "Dodging Inktober", "Linko": "/scribbles/231004-inktober-4", "Image" :"/dodge.jpeg"},
//   {"Title": "Penang old town hall", "Linko": "/scribbles/230621-penang-town-hall", "Image": "/230621-penang-town-hall.jpeg"},
//   {"Title": "Uncle E", "Linko": "/scribbles/230315_uncle_e", "Image": '/uncle_e.jpg'},
//   {"Title": "Hobart harbour", "Linko": "/scribbles/2302_hobart_harbour", "Image": "/2302_hobart_harbour.jpg"},
//   {"Title": "A very sunny day in Geelong", "Linko": "/scribbles/geelong_scribble", "Image": "/geelong_pier.jpg"},
//   {"Title": "Might be missing Sydney", "Linko": "/scribbles/240124-sydney-ferry", "Image": "/240124-sydney-ferry.jpg"},
   
// ]

let data = {"posts":
[
  {"title": "A couple more Inktobers", "slug": "231024-couple-more-inktobers", "preview":{ "html" :"/couplemoreinktobers.jpeg"}},
  {"title": "Penang old town hall", "slug": "230621-penang-town-hall", "preview":{"html": "/230621-penang-town-hall.jpeg"}},
  {"title": "Uncle E", "slug": "230315_uncle_e", "preview":{"html": '/uncle_e.jpg'}},
  {"title": "Hobart harbour", "slug": "2302_hobart_harbour", "preview":{"html": "/2302_hobart_harbour.jpg"}},
  {"title": "A very sunny day in Geelong", "slug": "geelong_scribble", "preview":{"html": "/geelong_pier.jpg"}},
  {"title": "Might be missing Sydney", "slug": "240124-sydney-ferry", "preview":{"html": "/240124-sydney-ferry.jpg"}},
]}

  //  console.log('data.posts: ', data.posts.preview)



</script>

<svelte:head>
  <title>{name}</title>
  <!-- <meta name="description" content={bio} /> -->
</svelte:head>

<div class="block max-w-3xl mx-auto display:block">
    <!-- class="prose w-full rounded" -->
    <div class='float-left mx-auto pr-4 prose rounded'>
    <!-- <img alt='about image' src='/about.png' class="max-w-50px rounded"/> -->
      <img alt='about image' src='/new_about.jpg' class="max-h-[15rem] text-wrap  mx-auto rounded sm:rounded-2xl"/>


    </div>


    <div class='pl-20px pb-2 text-wrap '>
      <br>
      <p>Ello.</p><br>
      <!-- , <a href='https://joshnicholas.com/projects'>projects</a> I'm working on -->
      <p>My name is <span class="font-semibold">Josh</span>. I love learning. </p><br>

      <p>This site hosts what would otherwise be more ephemeral - what I’m <a href='https://joshnicholas.com/words'>reading</a> and <a href='https://joshnicholas.com/scribbles'>scribbling</a> etc. Sort of like a public scrapbook.</p><br>

      <!-- <p>The site is pretty old now and has been through so many forms that many links etc. are broken.</p><br> -->
      <!-- <p>I am a data journalist at <a rel="noreferrer" href='https://www.theguardian.com/profile/josh-nicholas' target='_blank'>The Guardian</a>. Before that I covered <a href='https://theconversation.com/speaking-with-law-professor-cass-sunstein-on-why-behavioural-science-is-always-nudging-us-101074' rel="noreferrer" target='_blank'>economics</a> and technology, and made <a href='https://www.thewire.org.au/about/team/alumni/' rel="noreferrer" target='_blank'>podcasts and radio</a>.</p><br> -->

      <!-- <p>This site was built with an earlier version of <a rel="noreferrer" href='https://github.com/joshnicholas/sk-blog' target='_blank'>Sveltekit</a>. An API change could break it any day now. Content is also being programmatically pulled from other places. As a result some links, line breaks, quotes etc., may be janky.</p><br> -->

      <p>I post more regularly on <a rel="me" href='https://micro.blog/JoshNicholas' target='_blank'>micro.blog</a>. You can also follow me on <a href='https://bsky.app/profile/joshnicholas.com' target='_blank'>Bluesky</a> or at my day job at <a rel="noreferrer" href='https://www.theguardian.com/profile/josh-nicholas' target='_blank'>The Guardian</a>.<br>
    
      </div>

</div>


<div class=" clear-left block">
  <p class="pt-5 pb-10 text-center">
  Some current favourites:
  </p>
</div>





<div class="max-w-3xl mx-auto block">

<div class="flex flex-col flex-wrap flex-grow max-w-4xl pt-10 mx-auto">

  <PostsList posts={data.posts} />
</div>

</div>
<!-- <div class="container pt-5 grid grid-cols-1 grid-cols-2 gap-2 mx-auto items-center">

  {#each selected as example}


    <div class="text-base font-semibold tracking-tight text-zinc-800 dark:text-zinc-100">

      <a href={example.Linko}>
      <span class="absolute z-20 -inset-y-6 -inset-x-4 sm:-inset-x-6 sm:rounded-2xl" />
      <span class="relative z-10 text-xs mt-8 font-semibold text-zinc-800 dark:text-zinc-100">
        {example.Title}
      </span>
      </a>

      <div class="prose w-full rounded">
        <a href={example.Linko}>
        <img src={example.Image} alt={example.Title}>
          </a>
      </div>
      
    </div>

  {/each}



</div> -->


<!-- <Recents urlo={'https://joshnicholas.blog/feed.json'} /> -->

<style>
  a {
    color: #84cc16
  }
</style>
