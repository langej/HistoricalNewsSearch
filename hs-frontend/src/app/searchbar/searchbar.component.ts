import { Component, OnInit } from '@angular/core';
import {ActivatedRoute, Router} from "@angular/router";
import {SearchService} from "../shared/search.service";
import Axios from 'axios';

@Component({
  selector: 'hs-searchbar',
  templateUrl: './searchbar.component.html',
  styleUrls: ['./searchbar.component.css']
})
export class SearchbarComponent implements OnInit {

  query: string;

  recommendations: string[];

  constructor(private router: Router, private activeRoute: ActivatedRoute) {
    this.activeRoute.queryParams.subscribe(params => {
      this.query = params["q"];
    });
  }

  ngOnInit() {
    let input = document.getElementById('search-input');
    input.addEventListener("input", (event: any) => {
      Axios.get(`http://localhost:5000/recommendation/${event.target.value}`).then(
        response => {
          this.recommendations = [];
          response.data.map(
            elem => {
              this.recommendations.push(elem[0]);
            }
          );
          console.log(this.recommendations);
        }
      )
    })
  }

  navigate() {
    this.router.navigate(["/search"], { queryParams: { q: this.query }});
  }


}
