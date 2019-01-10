import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from "./home/home.component";
import { ResultListComponent } from "./result-list/result-list.component";
import { NewspaperDetailComponent } from "./newspaper-detail/newspaper-detail.component";

const routes: Routes = [
  {
    path: "",
    component: HomeComponent
  },
  {
    path: "search",
    component: ResultListComponent
  },
  {
    path: "newspaper/:id",
    component: NewspaperDetailComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
  providers: []
})
export class AppRoutingModule { }
