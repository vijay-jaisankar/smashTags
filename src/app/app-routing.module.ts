import { Component, NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomePageComponent } from './components/home-page/home-page.component';
import { UploadDocumentsComponent } from './upload-documents/upload-documents.component';
import { PostComponent } from './components/post/post.component';
import { ShowPostsComponent } from './components/show-posts/show-posts.component';
import { LandingComponent } from './components/landing/landing.component';

const routes: Routes = [
  {
    path: "",
    component: LandingComponent
  },
  {
    path: "home",
    component: HomePageComponent
  },
  {
    path: "upload",
    title: "Upload Documents-Smash Tags",
    component: UploadDocumentsComponent
  },
  {
    path: "post",
    component: PostComponent
  },
  {
    path: "show-posts",
    component: ShowPostsComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
