import {Component, Input, OnInit} from '@angular/core';
import {Newspaper} from "../shared/Newspaper";
import { encodeUriQuery } from '@angular/router/src/url_tree';
import { EvaluationElement } from '../shared/EvaluationElement';
import { Router } from '@angular/router';

@Component({
  selector: 'hs-result-element',
  templateUrl: './result-element.component.html',
  styleUrls: ['result-element.component.css']
})
export class ResultElementComponent implements OnInit {

  @Input()
  newspaper: Newspaper;

  @Input()
  index: number;
  relevant: boolean;
  evaluated: boolean;

  @Input()
  displayEvaluation: boolean;

  constructor(private router: Router) {}

  ngOnInit() {
    const item: EvaluationElement = JSON.parse(localStorage.getItem(`evaluation-${this.index}`));
    this.evaluated = item.evaluated;
    this.relevant = item.relevant;
  }

  navigateToDetails() {
    this.router.navigate([`/newspaper/${this.newspaper.id}`]);
  }

  evaluate(relevant: boolean) {
    const evaluationElement: EvaluationElement = JSON.parse(localStorage.getItem(`evaluation-${this.index}`));
    if (relevant) {
      evaluationElement.relevant = true;
      this.relevant = true;
    } else {
      evaluationElement.relevant = false;
      this.relevant = false;
    }
    evaluationElement.evaluated = true;
    this.evaluated = true;
    localStorage.setItem(`evaluation-${this.index}`, JSON.stringify(evaluationElement));
  }

}
