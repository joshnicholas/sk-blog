<script>
  // export const prerender = true;
    // import NewGallery from '$lib/components/newGallery.svelte'
  // import ScribblesList from '$lib/components/ScribblesList.svelte';
  import Recents from '$lib/components/recents.svelte';

  import PostsList from '$lib/components/ScribblesList.svelte'
  let stem = 'scribbles'

    import '../app.css'
  import '../prism.css'
  import { name } from '$lib/info.js'



	/** @type {import('./$types').PageData} */
	export let data;
// console.log("data: ", data.latest)


// let selected = [
//   {"Title": "Dodging Inktober", "Linko": "/scribbles/231004-inktober-4", "Image" :"/dodge.jpeg"},
//   {"Title": "Penang old town hall", "Linko": "/scribbles/230621-penang-town-hall", "Image": "/230621-penang-town-hall.jpeg"},
//   {"Title": "Uncle E", "Linko": "/scribbles/230315_uncle_e", "Image": '/uncle_e.jpg'},
//   {"Title": "Hobart harbour", "Linko": "/scribbles/2302_hobart_harbour", "Image": "/2302_hobart_harbour.jpg"},
//   {"Title": "A very sunny day in Geelong", "Linko": "/scribbles/geelong_scribble", "Image": "/geelong_pier.jpg"},
//   {"Title": "Might be missing Sydney", "Linko": "/scribbles/240124-sydney-ferry", "Image": "/240124-sydney-ferry.jpg"},
   
// ]

let posters = {"posts":
[
  {"title": "Yet more phones", "slug": "240413_yet_more_phones", "preview":{"html": "/240413_yet-more-phones_counter.jpg"}},
{"title": "Rained out of Sydney", "slug": "240117-misty-sydney-cbd", "preview":{"html": "/240117-misty-sydney-cbd.jpg"}},

  {"title": "A couple more Inktobers", "slug": "231024-couple-more-inktobers", "preview":{ "html" :"/couplemoreinktobers.jpeg"}},
  {"title": "Penang old town hall", "slug": "230621-penang-town-hall", "preview":{"html": "/230621-penang-town-hall.jpeg"}},
  {"title": "Uncle E", "slug": "230315_uncle_e", "preview":{"html": '/uncle_e.jpg'}},
  {"title": "Hobart harbour", "slug": "2302_hobart_harbour", "preview":{"html": "/2302_hobart_harbour.jpg"}},

]}


  //  console.log('data.posts: ', data.posts.preview)



</script>

<svelte:head>
  <title>{name}</title>
  <!-- <meta name="description" content={bio} /> -->
</svelte:head>

<div class="block max-w-3xl display:block">
    <!-- class="prose w-full rounded" -->
    <div class='float-left lg:w-1/3  prose rounded md:pr-10'>
    <!-- <img alt='about image' src='/about.png' class="max-w-50px rounded"/> -->
      <!-- <img alt='about image' src='/new_about.jpg' class="max-h-[15rem] text-wrap  mx-auto rounded sm:rounded-2xl"/> -->
      <img alt='about image' src='/yellow.jpg' class=" md:max-h-[25rem] mx-auto rounded rounded-2xl"/>


    </div>

  </div>
  <div class="block max-w-3xl mx-auto display:block">  
    <div class=''>
      <br>
      <br>

      <p>Ello.</p><br>
      <!-- , <a href='https://joshnicholas.com/projects'>projects</a> I'm working on -->
      <p>My name is <span class="font-semibold">Josh</span>. I'm a learner and scribbler. </p><br>

      <!-- <p>This site hosts what would otherwise be more ephemeral - what I’m <a href='https://joshnicholas.com/words'>reading</a> and <a href='https://joshnicholas.com/scribbles'>scribbling</a> etc. Sort of like a public scrapbook.</p><br> -->

      <p>This site is relatively ancient (I started it in high school) and has been through so many platforms, frameworks and other iterations that much of it is outdated or broken.</p><br>
      
      <!-- <p>If you scroll back far enough you can find some the first <a href='http://joshnicholas.com/scribbles/page/47'>scribbles</a> I posted.</p><br> -->
      <p>It is now mostly a <a href='#recents'>feed</a> of things I've made, done or posted elsewhere.</p><br>
      <!-- <p>I am a data journalist at <a rel="noreferrer" href='https://www.theguardian.com/profile/josh-nicholas' target='_blank'>The Guardian</a>. Before that I covered <a href='https://theconversation.com/speaking-with-law-professor-cass-sunstein-on-why-behavioural-science-is-always-nudging-us-101074' rel="noreferrer" target='_blank'>economics</a> and technology, and made <a href='https://www.thewire.org.au/about/team/alumni/' rel="noreferrer" target='_blank'>podcasts and radio</a>.</p><br> -->

      <!-- <p>This site was built with an earlier version of <a rel="noreferrer" href='https://github.com/joshnicholas/sk-blog' target='_blank'>Sveltekit</a>. An API change could break it any day now. Content is also being programmatically pulled from other places. As a result some links, line breaks, quotes etc., may be janky.</p><br> -->

      <!-- <p>I post more regularly on <a rel="me" href='https://micro.blog/JoshNicholas' target='_blank'>micro.blog</a>. You can also follow my posts on <a href='https://bsky.app/profile/joshnicholas.com' target='_blank'>Bluesky</a> or find my work at <a rel="noreferrer" href='https://www.theguardian.com/profile/josh-nicholas' target='_blank'>The Guardian</a>.<br> -->
    
      </div>

</div>


<div class=" clear-left block">
  <p class="pt-5 pb-10 text-center font-semibold">
  Some current favourites:
  </p>
</div>





<div class="max-w-3xl mx-auto block">

<div class="flex flex-col flex-wrap flex-grow max-w-3xl pt-10 mx-auto">

  <PostsList posts={posters.posts} />
</div>


  <p class="pt-10 pb-2 text-center font-semibold ">
    <a name='recents' class='font-semibold '>
    Recent stuff:
  </a>
  </p>
  <p class="text-sm text-center pb-10">(This is automated and updates once daily)</p>

<!-- <div class="container pt-5 grid grid-cols-1 grid-cols-2 gap-2 mx-auto items-center">

  {#each selected as example}


    <div class="text-base font-semibold tracking-tight ">

      <a href={example.Linko}>
      <span class="absolute z-20 -inset-y-6 -inset-x-4 sm:-inset-x-6 sm:rounded-2xl" />
      <span class="relative z-10 text-xs mt-8 font-semibold ">
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


<!-- <Recents urlo={'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/feed/latest.json'} />-->

<Recents recents={data.latest} />
</div>

<style>
  /* a {
    color: #FF9700
  } */


</style>
